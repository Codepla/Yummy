function get(url){
    /*we can use it to get data from server*/

    if(!url || typeof url != "string"){
        console.log("URL格式不正确");
    }
    $.ajax({
        url,
        dataType='json',
        function(data,status){
            if(status="success"){
                return data;
            }else{
                console.log("请求失败"+status);
            }
        }
    });
}

//TODO

function post(url,data){
    /*we can use it to post data to server*/
    //TODO
    console.log("TEST");
}