<template>
    <Booklist
        title="下载排行榜"
        :total="books.total"
        :books="books.selected"
        :page="page"
        :per-page="perPage"
    />
</template>
<script>
import Booklist from "@/components/Booklist";

export default {
    name: "Home",
    components: { Booklist },
    computed: {
        page() {
            return this.$route.query.page ? +this.$route.query.page : 1;
        },
        perPage() {
            return this.$route.query.perPage ? +this.$route.query.perPage : 10;
        },
        books() {
            return this.$store.getters["mostDownloadedBooks"](
                this.page,
                this.perPage
            );
        },
    },
};
</script>
