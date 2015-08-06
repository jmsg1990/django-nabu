var staticRoot = window.staticRoot ? window.staticRoot : '';

angular.module('nabuAdmin', [])
  .controller('nabuEditor', ['$scope', function($scope) {

    $scope.nabuData = window.nabuData ? JSON.parse(window.nabuData) : {}

    console.log($scope.nabuData);
  }])
  .directive('nabuForm', function() {
    return {
      templateUrl: staticRoot + 'js/templates/nabu-form.html'
    }
  })
;
