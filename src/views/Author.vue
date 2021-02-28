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
    name: "Author",
    components: { Booklist },
    props: {},
    computed: {
        page() {
            return this.$route.query.page ? +this.$route.query.page : 1;
        },
        perPage() {
            return this.$route.query.perPage ? +this.$route.query.perPage : 10;
        },
        books() {
            return this.$store.getters["getBooksByAuthor"](
                this.$route.params.name,
                this.page,
                this.perPage
            );
        },
        title() {
            return `${this.$route.params.name} 的作品`;
        },
    },
    data() {
        return {};
    },
    mounted: function () {},
    methods: {},
};
</script>