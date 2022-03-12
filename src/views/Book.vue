<template>
    <div class="book" v-if="bookIntro">
        <h2 class="title">
            <span
                >{{ bookIntro.title }}
                <span v-if="book.chapters?.length">
                    <a
                        class="btn btn-sm"
                        data-toggle="collapse"
                        href="javascript:;"
                        role="button"
                        aria-expanded="false"
                        aria-controls="collapseExample"
                        title="简介"
                        @click="showIntro = !showIntro"
                    >
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 24 24"
                            style="width: 16px; height: 16px"
                        >
                            <path
                                style="fill: #2196f3"
                                d="M 7.4296875 9.5 L 5.9296875 11 L 12 17.070312 L 18.070312 11 L 16.570312 9.5 L 12 14.070312 L 7.4296875 9.5 z"
                            ></path>
                        </svg>
                    </a>
                    <a
                        v-if="book.chapters?.length"
                        class="btn btn-sm"
                        role="button"
                        title="章节"
                        @click="showIntro = !showIntro"
                    >
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 24 24"
                            style="width: 24px; height: 24px"
                        >
                            <path
                                style="fill: #2196f3"
                                d="M 3 4.5 A 1.5 1.5 0 0 0 1.5 6 A 1.5 1.5 0 0 0 3 7.5 A 1.5 1.5 0 0 0 4.5 6 A 1.5 1.5 0 0 0 3 4.5 z M 7 5 L 7 7 L 22 7 L 22 5 L 7 5 z M 3 10.5 A 1.5 1.5 0 0 0 1.5 12 A 1.5 1.5 0 0 0 3 13.5 A 1.5 1.5 0 0 0 4.5 12 A 1.5 1.5 0 0 0 3 10.5 z M 7 11 L 7 13 L 22 13 L 22 11 L 7 11 z M 3 16.5 A 1.5 1.5 0 0 0 1.5 18 A 1.5 1.5 0 0 0 3 19.5 A 1.5 1.5 0 0 0 4.5 18 A 1.5 1.5 0 0 0 3 16.5 z M 7 17 L 7 19 L 22 19 L 22 17 L 7 17 z"
                            ></path>
                        </svg>
                    </a>
                </span>
            </span>
            <Downloadlink :book="bookIntro" />
        </h2>
        <authorlink
            :author="bookIntro.author"
            :category="bookIntro.category"
            :category-cn="Categories[bookIntro.category]"
        />
        <div class="collapse" id="collapseIntro" :class="{ show: showIntro }">
            <div class="card card-body">
                {{ bookIntro.description }}
            </div>
        </div>
        <div class="book_details" :class="{ loading: bookLoading }">
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
                        <router-link :to="`/book/${serie.serie_id}`">{{
                            serie.serie_title
                        }}</router-link>
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
            showIntro: false,
        };
    },
    title() {
        return this.bookIntro?.title;
    },
    computed: {
        ...mapState(["bookLoading"]),
        bookIntro() {
            return this.$store.getters["getBookIntroById"](this.id);
        },
        book() {
            return this.$store.getters["book"];
        },
        Categories() {
            return Categories;
        }
    },
    methods: {
        downloadEbook: function (bookId) {
            this.$store.dispatch("downloadEbook", bookId);
        },
        downloadPdf: function (bookId) {
            this.$store.dispatch("downloadPdf", bookId);
        },
    },
    beforeCreate() {
        this.$store.dispatch("loadChapters", this.id);
    },
    watch: {
        $route(route) {
            this.$store.dispatch("loadChapters", route.params.id);
        },
    },
};
</script>
<style lang="scss">
h4 {
    margin: 2rem 0 1rem 1rem;
}
.book_details {
    position: relative;
    min-height: 400px;
    &.loading::after {
        top: 200px;
    }
}
.book h2.title {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    justify-content: space-between;
    position: sticky;
    top: 50px;
    background: var(--book-bg);
    opacity: 0.96;
}
.card {
    background: none;
}
</style>