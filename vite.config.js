import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        VitePWA({
            registerType: 'autoUpdate',
            injectRegister: 'auto',
            workbox: {
                cleanupOutdatedCaches: false,
                globPatterns: ['**/*.{js,css,html,ico,png,svg,json,vue,txt,woff2}']
            }, manifest: {
                name: "Dushu App",
                short_name: "dushu",
                description: "读书--提供中国名著、外国名著、古典名著、儿童文学、经典故事、教育励志、诗词、散文、名人传记",
                theme_color: "#4DBA87",
                start_url: "/",
                display: "standalone",
                background_color: "#4DBA87",
                icons: [
                    {
                        src: "./img/icons/android-chrome-192x192.png",
                        sizes: "192x192",
                        type: "image/png",
                    },
                    {
                        src: "./img/icons/android-chrome-512x512.png",
                        sizes: "512x512",
                        type: "image/png",
                    },
                    {
                        src: "./img/icons/android-chrome-maskable-192x192.png",
                        sizes: "192x192",
                        type: "image/png",
                        purpose: "maskable"
                    },
                    {
                        src: "./img/icons/android-chrome-maskable-512x512.png",
                        sizes: "512x512",
                        type: "image/png",
                        purpose: "maskable"
                    }
                ],
            },
        })
    ],
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src'),
        },
        extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json', '.vue'],
    }
})