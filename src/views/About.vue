<template>
    <div class="about">
        <h2>
            {{ categoryCn }}
            <span>(共{{ books?.total }}部)</span>
        </h2>
        <div class="books mb-5">
            <Bookintro
                v-for="book in books?.selected"
                :key="book.id"
                :book="book"
            />
        </div>
        <Paginator
            :page="page"
            :total="books.total"
            :per-page="perPage"
            @pageChange="onPageChange"
        />
    </div>
</template>
<script>
import Bookintro from "@/components/Bookintro";
import Paginator from "@/components/Paginator";

export default {
    inject: ["Categories"],
    name: "About",
    components: { Bookintro, Paginator },
    props: {},
    computed: {
        page() {
            return this.$route.query.page ? +this.$route.query.page : 1;
        },
        perPage() {
            return this.$route.query.perPage ? +this.$route.query.perPage : 10;
        },
        books() {
            return this.$store.getters["getBooksByCategory"](
                this.$route.params.category,
                this.$route.query.page ? this.$route.query.page : 1,
                this.perPage
            );
        },
        categoryCn() {
            return this.Categories[this.$route.params.category];
        },
    },
    data() {
        return {};
    },
    methods: {
        onPageChange: function (page) {
            const query = { ...this.$route.query };
            query.page = page;
            query.perPage = this.perPage;
            this.$router.replace({
                name: "About",
                params: this.$route.params,
                query: query,
            });
        },
    },
    watch: {},
    mounted: function () {
        console.log("reload");
    },
};
</script>