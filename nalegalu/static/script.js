// $http.post('http://127.0.0.1:8000/search',  { 'message' : message });

angular.module('nalegaluApp.controllers', []).
controller('searchController', function($scope, $http) {
    $scope.searchList = [
      // {
      //       "full_title": "Cztery noce z Anną",
      //       "iplex": "",
      //       "ipla": "",
      //       "tvp": "http://vod.tvp.pl//filmy-fabularne/dramat/cztery-noce-z-anna"
      //   }

    ];

$scope.emptyS = "";

    $scope.clickEventFunction = function (){
        var query = {query:$scope.query};
        $http.post('http://127.0.0.1:8000/search', query).success(
                function (data){
                    console.log(data.items);
                    $scope.searchList = data.items;
                }
            );
    }
});


angular.module('nalegaluApp', [
  'nalegaluApp.controllers'
]);