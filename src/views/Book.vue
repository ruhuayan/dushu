<template>
    <div class="book" v-if="bookIntro">
        <h2 class="title">
            <span>{{ bookIntro.title }}</span>
            <div class="downloaded_count">
                <div class="download_ebook_count">
                    Ebook下载次数:
                    <span>{{ bookIntro.download_ebook_count }}</span> (<a
                        :href="`/ebooks/${bookIntro.title}/${bookIntro.title}.mobi`"
                        @click="downloadEbook(bookIntro.id)"
                        >下载</a
                    >)
                </div>
                <div class="download_pdf_count">
                    PDF下载次数:
                    <span>{{ bookIntro.download_pdf_count }}</span> (<a
                        :href="`/ebooks/${bookIntro.title}/${bookIntro.title}.pdf`"
                        target="_blank"
                        @click="downloadPdf(bookIntro.id)"
                        >下载</a
                    >)
                </div>
            </div>
        </h2>
        <div class="author_category">
            <div class="author">
                <span>作者：</span>
                <router-link
                    :to="'/author/' + bookIntro.author"
                    v-if="bookIntro.author"
                >
                    {{ bookIntro.author }}
                </router-link>
                <span v-else>无名</span>
            </div>
            <div class="category">
                <span>种类：</span>
                <router-link :to="`/about/${bookIntro.category}`">
                    {{ this.Categories[bookIntro.category] }}
                </router-link>
            </div>
        </div>

        <div class="desc">{{ bookIntro.description }}</div>
        <div class="book_details">
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
            <div
                class="chapters"
                v-if="book.chapters?.length"
                :set="(chapters = book.chapters)"
            >
                <div
                    class="chapter"
                    v-for="chapter in chapters"
                    :key="chapter.id"
                >
                    <h4>{{ chapter.title }}</h4>
                    <div class="chapter_desc" v-html="chapter.content"></div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    inject: ["Categories"],
    name: "Book",
    components: {},
    props: {},
    data() {
        return {};
    },
    computed: {
        bookIntro() {
            return this.$store.getters["getBookIntroById"](
                this.$route.params.id
            );
        },
        book() {
            return this.$store.getters["book"];
        },
    },
    mounted: function () {},
    methods: {
        downloadEbook: function (bookId) {
            this.$store.dispatch("downloadEbook", bookId);
        },
        downloadPdf: function (bookId) {
            this.$store.dispatch("downloadPdf", bookId);
        },
    },
    beforeCreate() {
        this.$store.dispatch("loadChapters", this.$route.params.id);
    },
};
</script>
<style lang="scss">
h4 {
    margin: 2rem 0 1rem 1rem;
}
.book h2.title {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    justify-content: space-between;
    position: sticky;
    top: 50px;
    background: var(--book-bg);
    opacity: 0.9;
}
</style>