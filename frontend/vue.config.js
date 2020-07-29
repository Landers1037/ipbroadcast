module.exports = {
	// publicPath: "./",
	outputDir: "dist",
    lintOnSave: false,
	assetsDir: 'static',
    publicPath: process.env.NODE_ENV === 'production'
        ? '/'
        : '/',
    runtimeCompiler: false,
	productionSourceMap: false,
    devServer: {
        port: 8080,
        proxy: {
            //默认的api路径就直接写根目录，后期调试在改为/api
            '/api': {
                target: 'http://127.0.0.1:5000',
                changeOrigin: true,
                ws: false,
                pathRewrite: {
                    '^/api': '/api'
                },
            },

        },
    },
    chainWebpack: config => {
        config.module
            .rule('md')
            .test(/\.md/)
            .use('html-loader')
            .loader('html-loader')
            .end()
            .use('markdown-loader')
            .loader('markdown-loader')
            .end()
    },
    configureWebpack: config =>{
	    config.entry.app = ["@babel/polyfill","./src/main.js"]
    }

}