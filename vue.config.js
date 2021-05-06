module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
        ? '/dushu/'
        : '/',
    chainWebpack: config => {
        config.plugins.delete('pwa');
        config.plugins.delete('workbox');
    }
}