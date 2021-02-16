<template>
    <div class="home">All Books</div>
</template>

<script>
import { Http } from "../http-common";
export default {
    name: "Home",
    components: {},
    props: {},
    data() {
        return {
            books: [],
        };
    },
    mounted: function () {
        Http.get(`most_downloaded_books`).then(
            (res) => (this.books = res.data)
        );
    },
    methods: {},
};
</script>
