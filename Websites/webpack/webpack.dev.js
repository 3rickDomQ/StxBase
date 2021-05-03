const path = require('path')
const webpack = require('webpack')
const MiniCSSExtract = require('mini-css-extract-plugin');

const merge = require('webpack-merge')

const backoffice = require('../backoffice/webpack/webpack.backoffice')
const public = require('../public/webpack/webpack.public')

const basePath = __dirname;
const distPath = '../share/assets/site/';


module.exports = (env, args) => {

    return merge(
        backoffice(args.mode),
        public(args.mode),
        {
            output: {
                path: path.join(basePath, distPath),
                filename: '[name].min.js'
            },
            module: {
                rules: [
                    {
                        test: /\.(js|jsx)$/,
                        exclude: /(node_modules|build)/,
                        use: ['babel-loader']
                    },
                    {
                        test: /\.(css|sass|scss)$/,
                        use: [
                            MiniCSSExtract.loader,
                            'css-loader',
                            'sass-loader'
                        ]
                    },
                    {
                        test: /\.(png|jpg|jpeg|svg|gif)$/,
                        use: [{
                            loader: 'file-loader'
                            // options: {
                            //     outputPath: distImages
                            // }
                        }]
                    },
                ]
            },
            plugins: [
                new MiniCSSExtract({
                    filename: '[name].min.css'
                }),
                new webpack.DefinePlugin({
                    PRODUCTION: (args.mode == 'production') ? true : false
                })
            ],
            devServer: {
                // This is where webpack-dev-server serves your bundle
                // which is created in memory.
                // To use the in-memory bundle,
                // your <script> 'src' should point to the bundle
                // prefixed with the 'publicPath', e.g.:
                //   <script src='http://localhost:9001/assets/bundle.js'>
                //   </script>
                publicPath: '/site/',
                contentBase: [
                    path.resolve(__dirname, '../share/assets/'),
                    path.resolve(__dirname, '../backoffice/templates/pages/'),
                ],
                watchContentBase: true,
                compress: true,
                host: '127.0.0.1',
                port: 9001,
                headers: {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
                    "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
                }
            }
        }
    )
}
