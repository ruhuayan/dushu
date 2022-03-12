<template>
    <Booklist
        :title="categoryCn"
        :total="books.total"
        :books="books.selected"
        :page="page"
        :per-page="perPage"
    />
</template>
<script>
import Booklist from "@/components/Booklist";
import { Categories } from '../models/categories';

export default {
    name: "About",
    components: { Booklist },
    title() {
        return this.categoryCn;
    },
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
                this.page,
                this.perPage
            );
        },
        categoryCn() {
            return Categories[this.$route.params.category];
        },
    },
};
</script>