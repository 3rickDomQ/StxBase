const path = require('path');
const MinifyPlugin = require('babel-minify-webpack-plugin');
const MiniCSSExtract = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const webpack = require('webpack')

const merge = require('webpack-merge');
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
                rules: [{
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
                new MinifyPlugin(),
                new MiniCSSExtract({
                    filename: '[name].min.css'
                }),
                new webpack.DefinePlugin({
                    PRODUCTION: (args.mode == 'production') ? true : false
                }),
                new webpack.DefinePlugin({ //<--key to reduce React's size
                    'process.env': {
                    'NODE_ENV': JSON.stringify('production')
                    }
                }),
                new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),
                new webpack.optimize.AggressiveMergingPlugin() //Merge chunks
            ],
            optimization: {
                minimizer: [
                    new OptimizeCSSAssetsPlugin({})
                ],
            }
        }
    )
}