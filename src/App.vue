<template>
    <Narbar :class="{ scrolled: navScrolled }" />
    <div class="container" :class="{ loading: loading }">
        <router-view />
    </div>
    <Footer />
    <svg display="none">
        <symbol width="14" height="14" viewBox="0 0 24 24" id="download">
            <path
                d="m12 16c-.205 0-.401-.084-.542-.232l-5.25-5.5c-.455-.476-.117-1.268.542-1.268h2.75v-5.75c0-.689.561-1.25 1.25-1.25h2.5c.689 0 1.25.561 1.25 1.25v5.75h2.75c.659 0 .997.792.542 1.268l-5.25 5.5c-.141.148-.337.232-.542.232z"
            />
            <path
                d="m22.25 22h-20.5c-.965 0-1.75-.785-1.75-1.75v-.5c0-.965.785-1.75 1.75-1.75h20.5c.965 0 1.75.785 1.75 1.75v.5c0 .965-.785 1.75-1.75 1.75z"
            />
        </symbol>
    </svg>
</template>

<style lang="scss">
:root {
    --book-bg: #faebd0;
}
.nav-link {
    color: var(--cyan);
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
        z-index: 100;
        &.scrolled {
            padding: 0 1rem;
            -webkit-box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.2);
            box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.2);
            .navbar-nav .nav-link {
                color: #fff;
            }
            input.search {
                background-color: #999;
                border: none;
                border-radius: 0;
                width: 250px;
                height: auto;
                padding: 0.2rem 0.3rem;
                color: #fff;
                &::placeholder {
                    color: #fff;
                    opacity: 0.9; /* Firefox */
                }
            }
            .btn-search {
                border: none;
                border-radius: 0;
                background-color: #999;
            }
            .dropdown-list {
                width: 290px;
                top: 40px;
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
            width: 180px;
        }
    }
    .downloaded_count {
        color: var(--gray);
        .download_ebook_count,
        .download_pdf_count {
            > span {
                margin-right: 0.5rem;
            }
            a svg {
                width: 14px;
                height: 14px;
                fill: var(--info);
                margin-top: -3px;
                &:hover {
                    fill: red;
                }
            }
        }
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
.loading::before {
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
.loading::after {
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
