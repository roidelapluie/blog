Title: R and Graphite
lang: en
Category: Monitoring
Tags: statistics, graphite, planet-inuits
Slug: r-and-graphite

[R](http://www.r-project.org/) is a famous language in the statistical world. It
has a large ecosystem and today I wanted to try to do some predictions with R and
Graphite.

    :::R
    library("rjson")
    library("RCurl")
    library("forecast")
    library("xts")

    metric <- "myhost.load.load.longterm"
    time <- "3days"
    host <- "graphite.example.com"

    url <- paste("https://", host, "/render/?target=", metric, "&format=json&from=-", time, sep="")[1]

    json_content <- getURL(url, userpwd="myuser:mypass", httpauth = 1L)
    json_data <- fromJSON(json_content)

    values <- c()

    datapoints <- json_data[[1]]$datapoints
    target <- json_data[[1]]$target

    for(d in datapoints){
        value <- (d[[1]])
        values <- c(values, value)
    }

    values <- ts(values, frequency=30)
    fit <- Arima(values, order=c(1,0,30))
    fcast <- forecast(fit)
    plot(fcast, main=target)


Result:

![R and Graphite](|filename|/images/r.png)

This POC could be improved of course, it was just to make some fun with R and predictions.

