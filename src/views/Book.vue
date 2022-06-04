<template>
    <div class="book" v-if="bookIntro">
        <div class="book-intro">
            <h2 class="title">
                {{ bookIntro.title }}
                <a
                    v-if="book.chapters?.length"
                    class="btn btn-sm chapter-link"
                    title="章节"
                    @click="toggle"
                    ref="chapterLink"
                >
                    <svg>
                        <use xlink:href="#arrow" />
                    </svg>
                    <span class="chapter-title">
                        {{ book.chapters[chapterIndex].title }}
                        <div
                            class="dropdown-list"
                            :class="{ show: showChapters }"
                        >
                            <div
                                v-for="chapter in book.chapters"
                                :key="chapter.chapter_id"
                                :id="'chapter-link_' + chapter.chapter_id"
                                :class="{
                                    active:
                                        chapter.chapter_id == chapterIndex + 1,
                                }"
                            >
                                <a :href="'#chapter_' + chapter.chapter_id">
                                    {{ chapter.title }}
                                </a>
                            </div>
                        </div>
                    </span>
                </a>
            </h2>
            <div class="book-intro_download">
                <authorlink
                    :author="bookIntro.author"
                    :category="bookIntro.category"
                    :category-cn="Categories[bookIntro.category]"
                />
                <Downloadlink :book="bookIntro" />
            </div>
        </div>
        <div class="book_details" :class="{ loading: bookLoading }">
            <div class="collapse show" id="chapter_0">
                <div class="card card-body">
                    {{ bookIntro.description }}
                </div>
            </div>
            <div
                class="chapters"
                v-if="book.series?.length"
                :set="(series = book.series)"
            >
                <div
                    class="chapter"
                    v-for="serie in series"
                    :key="serie.serie_title"
                >
                    <div class="chapter_title">
                        <router-link :to="`/book/${serie.serie_id}`">
                            {{ serie.serie_title }}
                        </router-link>
                    </div>
                </div>
            </div>
            <div class="chapters" v-if="book.chapters?.length">
                <div
                    class="chapter"
                    v-for="chapter in book.chapters"
                    :key="chapter.chapter_id"
                    :id="`chapter_${chapter.chapter_id}`"
                >
                    <h4>{{ chapter.title }}</h4>
                    <div class="chapter_desc" v-html="chapter.content"></div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { mapState } from "vuex";
import Authorlink from "@/components/Authorlink";
import Downloadlink from "@/components/Downloadlink";
import { Categories } from "../models/categories";

export default {
    name: "Book",
    components: { Authorlink, Downloadlink },
    props: {
        id: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            showChapters: false,
            chapterIndex: 0,
            scrollY: 0,
        };
    },
    title() {
        return this.bookIntro?.title;
    },
    computed: {
        ...mapState(["bookLoading", 'book']),
        bookIntro() {
            return this.$store.getters["getBookIntroById"](this.id);
        },
        Categories() {
            return Categories;
        },
    },
    methods: {
        downloadEbook: function (bookId) {
            this.$store.dispatch("downloadEbook", bookId);
        },
        downloadPdf: function (bookId) {
            this.$store.dispatch("downloadPdf", bookId);
        },
        toggle: function () {
            this.showChapters = !this.showChapters;
            if (this.showChapters) {
                const dd = document.querySelector(
                    ".chapter-title .dropdown-list"
                );
                setTimeout(() => {
                    dd.scrollTop = 21 * this.chapterIndex;
                });
            }
        },
        onScroll: function () {
            if (!this.book.chapters || !this.book.chapters.length) return;

            const fromTop = window.scrollY + 60;
            const chapters = document.querySelectorAll(".chapters .chapter");
            for (let i = 0; i < chapters.length; i++) {
                const section = chapters[i];

                if (
                    section.offsetTop <= fromTop &&
                    section.offsetTop + section.offsetHeight > fromTop
                ) {
                    this.chapterIndex = i;
                    return;
                }
            }
        },
        hideChpaterLinks: function (event) {
            if (this.$refs.chapterLink && !this.$refs.chapterLink.contains(event.target)) {
                this.showChapters = false;
            }
        },
    },
    beforeCreate() {
        this.$store.dispatch("loadChapters", this.id);
    },
    mounted: function () {
        document.addEventListener("click", this.hideChpaterLinks);
    },
    beforeUnmount: function () {
        this.$store.dispatch('setBookScrollY', {id: this.id, scrollY: window.scrollY});
    },
    unmounted: function () {
        document.removeEventListener("scroll", this.onScroll);
        document.removeEventListener("click", this.hideChpaterLinks);
    },
    watch: {
        $route(route) {
            if (route.params.id !== this.id && route.params.id) {
                this.$store.dispatch("loadChapters", route.params.id);
            }
        },
        book(newBook) {
            if (newBook.chapters?.length) {
                setTimeout(() => {
                    document.addEventListener("scroll", this.onScroll);
                    window.scrollTo(0, newBook.scrollY ?? 0);
                });
            }
        }
    },
};
</script>
<style lang="scss" scoped>
h4 {
    margin: 2rem 0 1rem 1rem;
}
.book_details {
    min-height: 400px;
    &.loading {
        height: 85vh;
        overflow: hidden;
    }
    &.loading::after {
        top: 200px;
    }
    .chapters > .chapter {
        padding-top: 80px;
        &:first-of-type {
            padding-top: 50px;
        }
        h4 {
            margin-top: 0;
        }
    }
}
.book .book-intro {
    position: sticky;
    top: 45px;
    background: var(--book-bg);
    opacity: 0.96;
    h2.title {
        display: flex;
        flex-wrap: wrap;
        align-items: baseline;
        margin-bottom: 0;
        a.chapter-link {
            text-align: left;
            svg {
                width: 12px;
                height: 16px;
                transition: all 0.1s ease-in-out;
                transform-origin: 4px 6px;
            }
            &:hover svg {
                transform: rotate(90deg);
            }
        }

        .chapter-title {
            margin-left: 0.2em;
        }

        .dropdown-list {
            position: absolute;
            text-align: left;
            margin-top: -32px;
            margin-left: -2px;
            overflow-y: auto;
            display: none;
            max-height: 400px;
            animation: fadein 0.5s linear normal;
            background: #fff;
            max-width: 400px;
            white-space: nowrap;
            overflow-x: hidden;
            z-index: 99;
            &.show {
                display: block;
            }
            &::-webkit-scrollbar {
                width: 6px;
            }
            > div {
                padding: 0 16px;
                &:first-child {
                    margin-top: 8px;
                }
                &:hover {
                    background: var(--gray-dark);
                    a {
                        color: #fff;
                    }
                }
            }

            div[id^="chapter-link_"] {
                height: 21px;
            }
            div.active {
                background: var(--gray-dark);
                a {
                    color: var(--light);
                }
            }
            a:hover {
                text-decoration: none;
            }
        }
    }
    .book-intro_download {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }
}

.card {
    background: none;
    position: unset;
}
@keyframes fadein {
    0% {
        opacity: 0;
    }
    30% {
        opacity: 0.1;
    }
    100% {
        opacity: 1;
    }
}
@media only screen and (max-width: 412px) {
    .book-intro h2.title {
        flex-direction: column;
        a.chapter-link {
            display: block;
        }
    }
}
</style>
