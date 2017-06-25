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

function ajaxPost(url,data,re_type){
    /*we can use it to post data to server*/
    var url = arguments[0] ? arguments[0] : '/index/';
    var data = arguments[1] ? arguments[1] : '{}';
    var re_type = arguments[2] ? arguments[2] : 'json';
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
                if(re_type=='json'){
                    return JSON.parse(data);
                }else{
                    return data;
                }
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

function setCookie(name,value){
    /* set cookies*/

    var Days = 30;
    var exp = new Date();
    exp.setTime(exp.getTime() + Days*24*60*60*1000);
    document.cookie = name + "="+ escape (value) + ";expires=" + exp.toGMTString();
}

function getCookie(name){
    /*get cookies*/
    var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
    if(arr=document.cookie.match(reg)){
        return unescape(arr[2]);
    }else{
        return null;
    }
}


function delCookie(name){
    /*delete cookies*/
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval=getCookie(name);
    if(cval!=null){
        document.cookie= name + "="+cval+";expires="+exp.toGMTString();
    }
}


//TODO