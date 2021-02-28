<template>
    <div class="booklist">
        <h2>
            {{ title }}
            <span>(共{{ total }}部)</span>
        </h2>
        <div class="books mb-5">
            <Bookintro v-for="book in books" :key="book.id" :book="book" />
        </div>
        <Paginator
            :page="page"
            :total="total"
            :per-page="perPage"
            @pageChange="onPageChange"
        />
    </div>
</template>
<script>
import Bookintro from "@/components/Bookintro";
import Paginator from "@/components/Paginator";

export default {
    name: "Booklist",
    components: { Bookintro, Paginator },
    props: {
        title: {
            type: String,
            required: true,
        },
        total: {
            type: Number,
            required: true,
        },
        books: {
            type: Array,
            required: true,
        },
        page: {
            type: Number,
            default: 1,
        },
        perPage: {
            type: Number,
            default: 10,
        },
    },
    computed: {},
    data() {
        return {};
    },
    methods: {
        onPageChange: function (page) {
            const query = { ...this.$route.query };
            query.page = page;
            query.perPage = this.perPage;
            this.$router.replace({
                name: this.$route.name,
                params: this.$route.params,
                query: query,
            });
        },
    },
    watch: {},
    mounted: function () {
        console.log("booklist loaded");
    },
};
</script>