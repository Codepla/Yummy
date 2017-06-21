function ajaxGet(url){
    /*we can use it to get data from server*/

    if(!url || typeof url != "string"){
        console.log("URL格式不正确");
    }
    var data_type = 'json';
    $.ajax({
        url,
        data_type,
        function(data,status){
            if(status="success"){
                try{
                    return JSON.parse(data);
                }catch(e){
                    console.debug("返回数据转为JSON失败");
                    return null;
                }
            }else{
                console.log("请求失败"+status);
            }
        }
    });
}

function ajaxPost(url,data){
    /*we can use it to post data to server*/
    if(!url || typeof url != "string"){
        console.log("URL格式不正确");
    }
    var request_data = "";
    try{
        request_data = JSON.stringify(data);
    }catch(e){
        console.debug("将请求JSON数据转化为字符串失败");
    }
    $.ajax({
        type: "POST",
        url: url,
        data: request_data,
        dataType: "json",
        success: function(data){
            try{
                return JSON.parse(data);
            }catch(e){
                console.debug("返回数据转为JSON失败");
                return null;
            }
        },
        error: function(jqXHR){
            alert("请求参数错误"+jqXHR.status);
            return null;
        }
    })
}

//TODO