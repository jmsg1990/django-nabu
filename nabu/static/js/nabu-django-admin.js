var staticRoot = window.staticRoot ? window.staticRoot : '';

angular.module('nabuAdmin', [])
  .controller('nabuEditor', ['$scope', function($scope) {

    $scope.nabuData = window.nabuData ? JSON.parse(window.nabuData.replace(/\n/g, '\\n')) : {}

    $scope.nabuGetterSetter = function(value) {
      // Don't set anything just return the serialized value
      return JSON.stringify($scope.nabuData);
    }
  }])
  .directive('nabuForm', ['$timeout', function($timeout) {
    return {
      templateUrl: staticRoot + 'js/templates/nabu-form.html',
      scope: {
        nabuData: '='
      },
      link: function($scope, $element) {
        var provider = document.querySelector('[name="provider"]').value;
        
        $scope.getTemplateUrl = function() {
          if (provider) {
            return staticRoot + 'js/templates/forms/' + provider + '.html'
          }
          return '';
        }
        
        document.querySelector('[name="provider"]').onchange = function() {
          $timeout(function() {
            provider = document.querySelector('[name="provider"]').value;
          });
        }

        $scope.$on('$destroy', function() {
          document.querySelector('[name="provider"]').onchange = null;
        });
      }
    }
  }])
  .directive('nabuArrayEditor', function() {
    return {
      templateUrl: staticRoot + 'js/templates/nabu-array-editor.html',
      scope: {
        model: '=',
      },
      link: function($scope, $element) {

        if (!$scope.model) { $scope.model = []; }

        $scope.addNewList = function() {
          $scope.model.push(['',])
        };
        
        $scope.addNewItem = function(idx) {
          $scope.model[idx].push('')
        };

        $scope.removeItem = function(listIdx, itemIdx) {
          $scope.model[listIdx].splice(itemIdx, 1);
          if (!$scope.model[listIdx].length) {
            $scope.model.splice(listIdx, 1);
          }
        }
      }
    }
  })
;
