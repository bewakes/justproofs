var webpack = require('webpack');
module.exports = {
    entry: "./assets/app/app.ts",
    output: {
        path: __dirname + "/assets/dist/js",
        filename: "bundle.js"
    },
    plugins:[
        new webpack.optimize.UglifyJsPlugin({
        compress: { warnings: false }
        })
    ],
    rules:[
    ],
    module: {
        loaders: [
            {loaders:['ts-loader']}
        ]
    },
};
