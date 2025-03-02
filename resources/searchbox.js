(function () {
    // 初始化 BaiduHttps 对象
    var BaiduHttps = window.BaiduHttps = {_option: {}};

    // 初始化检查函数
    var initCheck = function () {
        if (isNotIE6()) {
            loadHttpsCheckScript();
        } else {
            setProtocol("http");
        }
    };

    // 检查是否不是 IE6
    function isNotIE6() {
        var userAgent = navigator && navigator.userAgent ? navigator.userAgent : "";
        var ie6Regex = /msie 6/i;
        return !ie6Regex.test(userAgent);
    }

    // 加载 HTTPS 检查脚本
    function loadHttpsCheckScript() {
        appendScript({url: "https://www.baidu.com/con"});
    }

    // 设置协议和检查状态
    function setProtocol(protocol) {
        BaiduHttps._option.protocol = protocol;
        BaiduHttps._option.checked = true;
    }

    // 生成时间戳（16进制）
    function generateTimestampHex() {
        return new Date().getTime().toString(16);
    }

    // 动态添加脚本
    function appendScript(options) {
        var url = options.url || "https://www.baidu.com/con";
        var script = document.createElement("script");
        script.onload = function () {
        };
        script.onerror = function () {
            setProtocol("http");
        }; // 失败时使用 HTTP
        script.src = url + "?from=" + options.tn;
        document.body.appendChild(script);
    }

    // 处理脚本回调
    BaiduHttps.handleCallback = function (data) {
        if (typeof data === "object") {
            if (data.s == 0) {
                setProtocol("https"); // 状态 0 表示支持 HTTPS
            } else {
                setProtocol("http");
            }
        }
    };

    // 检查并返回 HTTPS 状态
    BaiduHttps.useHttps = function () {
        if (this._option.timeout === true) {
            initCheck(); // 重新触发检查
            this._option.timeout = false;
            setTimeout(function () {
                BaiduHttps._option.timeout = true;
            }, 1000 * 120); // 120秒后允许重新检查
        }
        if (this._option.checked && this._option.protocol == "https") {
            return {s: 1, ssl_code: "ssl10_" + generateTimestampHex()};
        } else {
            return {s: 0, ssl_code: "ssl9_" + generateTimestampHex()};
        }
    };

    // 初始调用检查
    initCheck();
})();

function checkHttps() {
    BaiduHttps.useHttps();
}

function baiduWithHttps(formname) {
    var data = BaiduHttps.useHttps();
    if (data.s === 0) {
        return true;
    } else {
        formname.action = 'https://www.baidu.com/baidu' + '?ssl_s=1&ssl_c' + data.ssl_code;
        return true;
    }
}