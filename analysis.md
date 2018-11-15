抖音协议分析
==========

> 由于只使用 as, cp的 libuserinfo.so老版本算法逻辑都能从网上查到, 这里就不做分析了 

## 版本信息

[v3.1.0](https://share.weiyun.com/5nuuGx4), 算法为新版 as, cp, mas算法

## 逆向过程

### JAVA层面

众所周知, 抖音v2版本的算法签名为  as, cp, mas, 使用AK/Jadx打开目标apk, 找到签名逻辑, 在 `com.ss.android.ugc.aweme.app.api.b` 这个类中, 其中签名的逻辑
为

```java
/**
 *  更多详细信息参见: http://hacksign.liebian.me
 */
public static HttpUrl a(HttpUrl httpUrl, List<String> list, int i) {
    if (PatchProxy.isSupport(new Object[]{httpUrl, list, new Integer(i)}, null, a, true, 4541, new Class[]{HttpUrl.class, List.class, Integer.TYPE}, HttpUrl.class)) {
        return (HttpUrl) PatchProxy.accessDispatch(new Object[]{httpUrl, list, new Integer(i)}, null, a, true, 4541, new Class[]{HttpUrl.class, List.class, Integer.TYPE}, HttpUrl.class);
        }
    String decode = URLDecoder.decode(httpUrl.toString());
    String c = d.c();
    String str = "";
    if (decode.contains("&device_id=") || decode.contains("?device_id=")) {
        if (TextUtils.isEmpty(c)) {
            c = (String) c(decode).get(x.u);
        }
        str = UserInfo.getUserInfo(i, (String[]) list.toArray(new String[list.size()]), null, c);
    } else {
        str = UserInfo.getUserInfo(i, (String[]) list.toArray(new String[list.size()]), null, "");
    }
    Builder newBuilder = httpUrl.newBuilder();
    int length = str.length();
    if (TextUtils.isEmpty(str)) {
        f.a(decode, (List) list, str, c, (long) i);
        newBuilder.addQueryParameter(AdvanceSetting.ADVANCE_SETTING, "a1iosdfgh").addQueryParameter("cp", "androide1");
    } else if (length % 2 == 0) {
        decode = str.substring(0, length >> 1);
        String substring = str.substring(length >> 1, length);
        str = "";
        a a = com.ss.sys.ces.f.b.a(GlobalContext.getContext(), (long) g.B().m());
        a.a(j.a());
        newBuilder.addQueryParameter(AdvanceSetting.ADVANCE_SETTING, decode).addQueryParameter("cp", substring).addQueryParameter("mas", k.a(a.a(decode.getBytes())));
        } else {
            f.a(decode, (List) list, str, c, (long) i);
            newBuilder.addQueryParameter(AdvanceSetting.ADVANCE_SETTING, "a1qwert123").addQueryParameter("cp", "cbfhckdckkde1");
        }
        return newBuilder.build();
}
```

通过这段代码我们可以了解到如下内容

> 调用 `com.ss.android.common.applog.UserInfo` 里的native 方法 `public static native String getUserInfo(int timestamp, String[] paramList, String[] strArr2, String deviceId)` 生成44位字符串, 前 22位给as, 后22位给cp
 
然后mas是调用 `com.ss.android.common.applog.k.a` 静态方法得来的, 参数为一个byte数组

```java
package com.ss.android.common.applog;
/**
 *  更多详细信息参见: http://hacksign.liebian.me
 */
public class k {
    public static String a(byte[] bArr) {
        if (PatchProxy.isSupport(new Object[]{bArr}, null, a, true, 282, new Class[]{byte[].class}, String.class)) {
            return (String) PatchProxy.accessDispatch(new Object[]{bArr}, null, a, true, 282, new Class[]{byte[].class}, String.class);
        } else if (bArr == null) {
            return null;
        } else {
            char[] toCharArray = "0123456789abcdef".toCharArray();
            char[] cArr = new char[(bArr.length * 2)];
            for (int i = 0; i < bArr.length; i++) {
                int i2 = bArr[i] & 255;
                cArr[i * 2] = toCharArray[i2 >>> 4];
                cArr[(i * 2) + 1] = toCharArray[i2 & 15];
            }
            return new String(cArr);
        }
    }
}
```

那么 `k.a(byte[] bArr)`的byte数组参数是哪里来的呢? 进一步发现是调用

`com.ss.sys.ces.f.a` 这个接口的 `byte[] a(byte[] bArr)` 方法计算的, 该接口的实现类为 `com.ss.sys.ces.b`, 进而发现实际调用的是 `com.ss.sys.ces.a`类中的navtie方法 `public static native byte[] e(byte[] bArr)`, 实现逻辑在 `libcms.so` 中


### Native层面
