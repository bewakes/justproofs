var webpack = require('webpack');
module.exports = {
    entry: "./assets/app/main.ts",
    output: {
        path: __dirname + "/assets/dist/js",
        filename: "bundle.js"
    },
    resolve: {
        extensions: ['', '.js', '.ts']
    },
    plugins:[
        new webpack.optimize.UglifyJsPlugin({
        compress: { warnings: false }
        })
    ],
    module: {
        loaders: [
            {
                test: /\.ts/,
                loaders: ['ts-loader'],
                exclude: /node_modules/
            }
        ]
    },
};
