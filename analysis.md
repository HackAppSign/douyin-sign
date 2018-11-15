抖音协议分析
==========

> 由于只使用 as, cp的 libuserinfo.so老版本算法逻辑都能从网上查到, 这里就不做分析了 

### 版本信息

[v3.1.0](https://share.weiyun.com/5nuuGx4), 算法为新版 as, cp, mas算法

### 逆向过程

众所周知, 抖音v2版本的算法签名为  as, cp, mas, 使用AK/Jadx打开目标apk, 找到签名逻辑, 在 `com.ss.android.ugc.aweme.app.api.b` 这个类中, 其中签名的逻辑
为

```
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

```
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
```

j.a的逻辑是取到一个cookie里的sessionId, 许多逆向的研究人员忽略了这一点

```
/* compiled from: SessionUtil */
public class j {
    public static ChangeQuickRedirect a;

    public static String a() {
        if (PatchProxy.isSupport(new Object[0], null, a, true, 4700, new Class[0], String.class)) {
            return (String) PatchProxy.accessDispatch(new Object[0], null, a, true, 4700, new Class[0], String.class);
        }
        try {
            String cookie = CookieManager.getInstance().getCookie(c.f);
            if (TextUtils.isEmpty(cookie)) {
                return "";
            }
            if (cookie.contains("sessionid=")) {
                for (String str : cookie.split(Constants.PACKNAME_END)) {
                    if (str.trim().startsWith("sessionid=")) {
                        return str.substring("sessionid=".length() + 1);
                    }
                }
            }
            return "";
        } catch (Throwable th) {
        }
    }
}
```


## 未完待续

```java
package com.ss.android.ugc.aweme.feed.api

/**
 *  更多详细信息参见: http://hacksign.liebian.me
 */
public class FeedApi {
    public static ChangeQuickRedirect a;
    static final RetrofitApi b = ((RetrofitApi) ((IRetrofitService) ServiceManager.get().getService(IRetrofitService.class)).createNewRetrofit(y.a).create(RetrofitApi.class));

    interface RetrofitApi {
        @f(a = "https://aweme.snssdk.com/aweme/v1/nearby/feed/")
        k<FeedItemList> fetchNearbyFeed(@t(a = "max_cursor") long j, @t(a = "min_cursor") long j2, @t(a = "count") int i, @t(a = "feed_style") Integer num, @t(a = "aweme_id") String str, @t(a = "filter_warn") int i2, @t(a = "city") String str2, @t(a = "latitude") String str3, @t(a = "longitude") String str4, @t(a = "poi_class_code") int i3);

        @f(a = "https://aweme.snssdk.com/aweme/v1/nearby/feed/")
        k<FeedItemList> fetchNearbyMockFeed(@t(a = "max_cursor") long j, @t(a = "min_cursor") long j2, @t(a = "count") int i, @t(a = "feed_style") Integer num, @t(a = "aweme_id") String str, @t(a = "filter_warn") int i2, @t(a = "city") String str2);

        @f(a = "https://aweme.snssdk.com/aweme/v1/poi/vertical/aweme/")
        k<FeedItemList> fetchPoiTypeFeeds(@t(a = "count") int i, @t(a = "feed_style") Integer num, @t(a = "filter_warn") int i2, @t(a = "city_code") String str, @t(a = "latitude") String str2, @t(a = "longitude") String str3, @t(a = "poi_class_code") int i3, @t(a = "cursor") long j);

        @f(a = "/aweme/v1/feed/")
        i<FeedItemList> fetchRecommendFeed(@t(a = "type") int i, @t(a = "max_cursor") long j, @t(a = "min_cursor") long j2, @t(a = "count") int i2, @t(a = "feed_style") Integer num, @t(a = "aweme_id") String str, @t(a = "volume") double d, @t(a = "pull_type") int i3, @t(a = "need_relieve_aweme") int i4, @t(a = "filter_warn") int i5, @t(a = "req_from") String str2, @t(a = "is_cold_start") int i6);

        @f(a = "https://aweme.snssdk.com/aweme/v1/fresh/feed/")
        k<FeedTimeLineItemList> fetchTimelineFeed(@t(a = "type") int i, @t(a = "max_time") long j, @t(a = "min_time") long j2, @t(a = "count") int i2, @t(a = "aweme_id") String str, @t(a = "filter_warn") int i3);
    }
    
    //Continue
}
```
