function changeCity() {
    //    1. 如何让存储省份和城市之间的关系?
    //    provinces = [["西安", "渭南", '宝鸡'], ["太原", "晋城"， ”大同“], ["桂林", "南宁"]]
    var provinces = new Array(3);
    provinces[0] = new Array("西安", "渭南", '宝鸡');
    provinces[1] = new Array("太原", "晋城", "大同");
    provinces[2] = new Array("桂林", "南宁");


    //    2. 获取用户选择的省份
    var choiceProvince = document.getElementById('province').value;  //0


    //     3. 遍历用户选择省份对应的所有城市
    var citys = provinces[choiceProvince];


    // 获取select节点对象
    var selectCityObj = document.getElementById('city');
    //清空select标签里面的所有内容;
    selectCityObj.length = 0;
    //      4. 并添加到select里面;
    for (var i = 0; i < citys.length; i++) {

        //  创建城市的文本节点;
        var textnode = document.createTextNode(citys[i]);  // "西安"
        // 创建option节点对象
        var optEleObj = document.createElement('option');
        // 将文本节点添加到option节点中
        optEleObj.appendChild(textnode);
        selectCityObj.appendChild(optEleObj);
    }


}