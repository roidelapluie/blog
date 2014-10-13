var articlesListControllers = angular.module('ArticleControllers', []);

articlesListControllers.controller('ArticleListCtrl', ['$scope', '$http', '$filter', '$routeParams', '$anchorScroll', '$location',

        function($scope,$http, $filter,$routeParams,$anchorScroll,$location) {
            $scope.itemsPerPage=4;
            $scope.currentPage=0;
            $scope.Math = window.Math;
            $http.get('data/articles.json').success(function(data) {
                $scope.contents = data;
                if ($routeParams.articleSlug) {
                    $scope.filtered_contents = $filter('filter')($scope.contents,{'slug':$routeParams.articleSlug});
                    $scope.articlesIndex=false;
                }else{
                $scope.title = "All articles";
                $scope.filtered_contents = $scope.contents;
                    $scope.articlesIndex=true;
                }
                $scope.content_filtered = false;
            });
            $scope.clearFilter = function(){
                $scope.filtered_contents = $scope.contents;
                $scope.title = "All articles";
                $scope.currentPage=0;
                $scope.content_filtered = false;
                    $scope.articlesIndex=true;
                    $location.hash('top');
                    $anchorScroll();
            }
            $scope.filterCategory = function(category){
                $scope.filtered_contents = $filter('filter')($scope.contents,{'category':category});
                $scope.title = "Articles in category \""+category+"\"";
                $scope.currentPage=0;
                $scope.content_filtered = true;
                    $scope.articlesIndex=true;
                    $location.hash('top');
                    $anchorScroll();
            };
            $scope.filterTag = function(tag){
                $scope.filtered_contents = $filter('filterTag')($scope.contents,tag);
                $scope.title = "Articles with tags \""+tag+"\"";
                $scope.currentPage=0;
                $scope.content_filtered = true;
                    $scope.articlesIndex=true;
                    $location.hash('top');
                    $anchorScroll();
            };


        }]);

articlesListControllers.controller('ArticleDetailCtrl', ['$scope', '$routeParams', '$http',
        function($scope,$routeParams,$http) {
            $http.get('data/articles.json').success(function(data) {
                $scope.contents = data;
                $scope.contentType = 'blog';
                $scope.pageSlug = $routeParams.pageSlug;
            });
        }]);

var pageControllers = angular.module('PageControllers', []);

pageControllers.controller('PageListCtrl', ['$scope', '$http',
        function($scope,$http) {
            $http.get('data/pages.json').success(function(data) {
                $scope.contents = data;
            });
        }]);

pageControllers.controller('PageDetailCtrl', ['$scope', '$routeParams', '$http',
        function($scope, $routeParams, $http) {
            $http.get('data/pages.json').success(function(data) {
                $scope.pageSlug = $routeParams.pageSlug;
                $scope.contentType = 'page';
                $scope.contents = data;
            })}]);

var blogApp = angular.module('blogApp', ['ngRoute', 'ngSanitize', 'ArticleControllers', 'PageControllers']);

blogApp.run(['$rootScope','$location', '$route', '$routeParams', function($rootScope, $location, $route, $routeParams) {
    $rootScope.$on('$routeChangeSuccess', function(e, current, pre) {
        if ($route.current.controller == "PageDetailCtrl") {
            if ($routeParams['pageSlug'] == "about-me") {
                $rootScope.currentSection="about";
            }
            else if ($routeParams['pageSlug'] == "disclaimer") {
                $rootScope.currentSection="disclaimer";
            }
            else {
                $rootScope.currentSection="wiki";
            }
        } else if ($route.current.controller == "PageListCtrl") {
            $rootScope.currentSection="wiki";
        } else if ($route.current.controller == "ArticleListCtrl") {
            $rootScope.currentSection="blog";
        } else if ($route.current.controller == "ArticleDetailCtrl") {
            $rootScope.currentSection="blog";
        }

    })}]);

blogApp.filter('offset', function() {
    return function(input, start) {
        if (!angular.isUndefined(input)) {
            start = parseInt(start, 10);
            return input.slice(start);
        }else{
            return input;
        }
    };
});

blogApp.filter('filterTag', function() {
    return function(articles, tag) {
        return articles.filter(function(article) {

            if (article.tags.indexOf(tag) != -1) {
                return true;
            }
            return false;

        })};
});

blogApp.config(['$routeProvider',
        function($routeProvider) {
            $routeProvider.
    when('/wiki', {
        templateUrl: 'angular/wiki.html',
    controller: 'PageListCtrl'
    }).
when('/blog', {
    templateUrl: 'angular/index.html',
controller: 'ArticleListCtrl'
}).
when('/blog/:pageSlug/changelog', {
    templateUrl: 'angular/changelog.html',
controller: 'ArticleDetailCtrl'
}).
when('/blog/:articleSlug/source', {
    templateUrl: 'angular/source.html',
controller: 'ArticleDetailCtrl'
}).
when('/blog/:articleSlug', {
    templateUrl: 'angular/index.html',
controller: 'ArticleListCtrl'
}).
when('/page/:pageSlug', {
    templateUrl: 'angular/page.html',
controller: 'PageDetailCtrl'
}).
when('/page/:pageSlug/changelog', {
    templateUrl: 'angular/changelog.html',
controller: 'PageDetailCtrl'
}).
when('/page/:pageSlug/source', {
    templateUrl: 'angular/source.html',
controller: 'PageDetailCtrl'
}).
otherwise({
    redirectTo: '/page/about-me'
});
}]);
