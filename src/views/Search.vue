<template>
    <Booklist
        :title="title"
        :total="books.total"
        :books="books.selected"
        :page="page"
        :per-page="perPage"
    />
</template>
<script>
import Booklist from "@/components/Booklist";
export default {
    name: "Search",
    components: { Booklist },
    title() {
        return this.title;
    },
    computed: {
        page() {
            return this.$route.query.page ? +this.$route.query.page : 1;
        },
        perPage() {
            return this.$route.query.perPage ? +this.$route.query.perPage : 10;
        },
        query() {
            return this.$route.query.book ? this.$route.query.book : "";
        },
        qtype() {
            return this.$route.query.qtype ? this.$route.query.qtype : "title";
        },
        books() {
            return this.$store.getters["getBooksByQuery"](
                this.query,
                this.qtype,
                this.page,
                this.perPage
            );
        },
        title() {
            return `搜索 "${this.query}" 的作品`;
        },
    },
};
</script>