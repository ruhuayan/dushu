<template>
    <div class="book">
        <div class="bookTitle">
            <router-link :to="`/book/${book.id}`">{{ book.title }}</router-link>
        </div>
        <div class="author_category">
            <div class="author">
                <span>作者：</span>
                <router-link :to="'/author/' + book.author" v-if="book.author">
                    {{ book.author }}
                </router-link>
                <span v-else>无名</span>
            </div>
            <div class="category" v-if="catShow">
                <span>种类：</span>
                <router-link :to="`/about/${book.category}`">
                    {{ this.Categories[book.category] }}
                </router-link>
            </div>
        </div>

        <div class="bookDesc">{{ book.description }}</div>
        <div class="downloaded_count">
            <div class="download_ebook_count">
                Ebook下载次数: <span>{{ book.download_ebook_count }}</span>
            </div>
            <div class="download_pdf_count">
                PDF下载次数: <span>{{ book.download_pdf_count }}</span>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    inject: ["Categories"],
    name: "Bookintro",
    components: {},
    props: {
        book: {
            type: Object,
            required: true,
        },
        catShow: {
            type: Boolean,
            default: true,
        },
    },
    computed: {},
    methods: {},
    mounted: function () {},
};
</script>