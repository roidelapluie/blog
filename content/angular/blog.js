var articlesListControllers = angular.module('ArticlesListControllers', []);

articlesListControllers.controller('ArticlesListCtrl', ['$scope', '$http',
      function($scope,$http) {
          $http.get('data/articles.json').success(function(data) {
              $scope.articles = articles;
      });
}]);

var pageControllers = angular.module('pageControllers', []);

pageControllers.controller('PageListCtrl', ['$scope', '$http',
      function($scope,$http) {
          $http.get('data/pages.json').success(function(data) {
              $scope.pages = pages;
      });
}]);

pageControllers.controller('PageDetailCtrl', ['$scope', '$routeParams',
          function($scope, $routeParams) {
                  $scope.pageSlug = $routeParams.pageSlug;
                    }]);

var blogApp = angular.module('blogApp', ['ngRoute', 'ArticlesListControllers']);


blogApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
        when('/blog', {
            templateUrl: 'angular/articles.html',
            controller: 'ArticlesListCtrl'
        }).
        when('/page/:pageSlug', {
            templateUrl: 'angular/pages.html',
            controller: 'PageDetailCtrl'
        }).
        otherwise({
            redirectTo: '/page/about-me'
        });
}]);
