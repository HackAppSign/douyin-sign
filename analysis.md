抖音协议分析
==========

> 由于只使用 as, cp的 libuserinfo.so老版本算法都能从网上查到, 这里就不做分析了 

### 版本信息

[v3.1.0](https://share.weiyun.com/5nuuGx4), 算法为新版 as, cp, mas算法

### 逆向过程

众所周知, 抖音v2版本的算法签名为  as, cp, mas, 使用AK/Jadx打开目标apk, 找到签名逻辑

https://carbon.now.sh


```java
package com.ss.android.ugc.aweme.feed.api

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
