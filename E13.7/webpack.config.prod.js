const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    mode: 'production', // Режим production 
    devtool: 'source-map', // Лучше использовать source-map для продакшн сборки
    entry: './src/index-prod.js',
    plugins: [
        new HtmlWebpackPlugin({
            title: 'Production',
        }),
    ],
    output: {
        filename: 'prodmain.js',
    },
    module: {
        rules: [
            {
                test: /\.pug$/,
                loader: 'pug-loader',
                options: {
                    pretty: true
                }
            }
        ]
    }
};
