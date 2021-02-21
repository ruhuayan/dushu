<template>
    <div class="author">
        <h2>
            {{ $route.params.name }} 的作品
            <span>(共{{ books.length }}部)</span>
        </h2>
        <div class="books">
            <Bookintro
                v-for="book in books"
                :key="book.id"
                :book="book"
                :cat-show="true"
            />
        </div>
    </div>
</template>
<script>
import Bookintro from "@/components/Bookintro";
export default {
    name: "Author",
    components: { Bookintro },
    props: {},
    computed: {
        books() {
            return this.$store.getters["getBooksByAuthor"](
                this.$route.params.name
            );
        },
    },
    data() {
        return {};
    },
    mounted: function () {},
    methods: {},
};
</script>