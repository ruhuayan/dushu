<template>
    <Narbar :class="{ scrolled: navScrolled }" />
    <div class="container" :class="{ loading: loading }">
        <router-view />
    </div>
    <Footer />
</template>

<style lang="scss">
:root {
    --book-bg: #faebd0;
}
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    // text-align: center;
    color: #2c3e50;

    background: var(--book-bg);

    nav.navbar {
        position: fixed;
        width: 100%;
        -webkit-transition: all 0.4s ease;
        transition: all 0.4s ease;
        &.scrolled {
            padding: 0 1rem;
            background-color: #efc47d !important;
            -webkit-box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.2);
            box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.2);
            .navbar-nav .nav-link {
                color: #fff;
            }
            input.search {
                background: none;
                border: none;
                border-radius: 0;
                border-bottom: 2px solid #fff;
                height: auto;
                padding: 0.2rem;
                color: #fff;
                &::placeholder {
                    color: #fff;
                    opacity: 0.9; /* Firefox */
                }
            }
        }
    }
    .container {
        padding-top: 90px;
    }
}
.container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    &.loading {
        min-height: 600px;
    }
    &.loading::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1000;
        width: 100%;
        height: 100%;
        background: var(--book-bg);
        opacity: 0.8;
    }
    &.loading::after {
        content: " ";
        position: absolute;
        margin-left: auto;
        margin-right: auto;
        z-index: 1001;
        left: 0;
        right: 0;
        top: 300px;
        transform: translateY(-50%);
        width: 30px;
        height: 30px;
        border-radius: 50%;
        border: 5px solid var(--gray);
        border-color: var(--gray) transparent var(--gray) transparent;
        animation: loader 1.2s linear infinite;
    }
    @keyframes loader {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
}
.book {
    margin-top: 1.5rem;
    .bookTitle {
        font-weight: bold;
    }
    .author_category,
    .downloaded_count {
        font-size: 12px;
        margin: 2px 0 5px 0;
        display: flex;
        // color: var(--info);
        .author,
        .download_ebook_count {
            width: 160px;
        }
    }
    .downloaded_count {
        color: #999;
    }
    .bookDesc {
        font-size: 0.9rem;
        border-top: solid 1px rgba(0, 0, 0, 0.05);
        border-bottom: solid 1px rgba(0, 0, 0, 0.05);
        padding: 0.5em 0.3em;
    }
    a {
        color: var(--cyan);
    }
}
</style>
<script>
import { mapState } from "vuex";
// @ is an alias to /src
import Narbar from "@/components/Narbar.vue";
import Footer from "@/components/Footer.vue";

export default {
    name: "App",
    components: { Narbar, Footer },
    computed: {
        ...mapState(["loading"]),
    },
    data() {
        return {
            navScrolled: false,
        };
    },
    mounted: function () {
        window.addEventListener("scroll", () => {
            const scrollBarPosition =
                window.pageYOffset | document.body.scrollTop;
            if (scrollBarPosition >= 10) {
                this.navScrolled = true;
            } else {
                this.navScrolled = false;
            }
        });
    },
    beforeCreate() {
        this.$store.dispatch("loadBooks");
    },
};
</script>
