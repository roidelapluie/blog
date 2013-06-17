Title: Grok and httpd
Date: 2013-06-17
Category: Monitoring
Tags: grok, logstash
Slug: grok-httpd

When you use the [`LogFormat`](http://httpd.apache.org/docs/current/mod/mod_log_config.html) parameter in you apache configuration, you may want to use the same logformat in logstash.

I made a small table that will enable you to ''translate'' your custom log format into a grok pattern.

| httpd | grok |
| ----- | ---- |
| `%T` | `%{NUMBER:duration_seconds}` |
| `%D` | `%{NUMBER:duration_microseconds}` |
| `%h` | `%{IPORHOST:client}` |
| `%l` | `%{USERNAME:remotelogname}` |
| `%u` | `%{USERNAME:username}` |
| `%t` | `\[%{HTTPDATE:timestamp}\]` |
| `%r` | `%{USERNAME:method} %{URIPATHPARAM:request} HTTP/%{NUMBER:httpversion}` |
| `%s` | `%{NUMBER:response}` |
| `%B` | `%{NUMBER:bytes}` |
| `%b` | `(?:%{NUMBER:bytes}|-)` |
| `\"%{Referer}i\"` | `%{QS:referer}` |
| `\"%{User-Agent}i\"` | `%{QS:useragent}` |
