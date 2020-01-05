  $("button#play").on('click', function(){
                 $.ajax({
                      type:'post',
                      url: '{{url}}{{play}}',
                      success: function(response) {
                        console.log(response)
                    }
               });
            });
            $("button#select").on('click', function(){
                 $.ajax({
                      type:'post',
                      url: '{{url}}{{select}}',
                      success: function(response) {
                        console.log(response)
                    }
               });
            });
            $("button#left").on('click', function(){
                 $.ajax({
                      type:'post',
                      url: '{{url}}{{left}}',
                      success: function(response) {
                        console.log(response)
                    }
               });
            });
            $("button#right").on('click', function(){
                 $.ajax({
                      type:'post',
                      url: '{{url}}{{right}}',
                      success: function(response) {
                        console.log(response)
                    }
               });
            });
            
            $("button#up").on('click', function(){
                 $.ajax({
                      type:'post',
                      url: '{{url}}{{up}}',
                      success: function(response) {
                        console.log(response)
                    }
               });
            });
            
            
            $("button#down").on('click', function(){
                 $.ajax({
                      type:'post',
                      url: '{{url}}{{down}}',
                      success: function(response) {
                        console.log(response)
                    }
               });
            });
            