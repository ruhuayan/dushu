<template>
    <div class="author">
        <h2>
            {{ $route.params.name }} 的作品
            <span>(共{{ books.length }}部)</span>
        </h2>
        <div class="books mb-5">
            <Bookintro
                v-for="book in books"
                :key="book.id"
                :book="book"
                :cat-show="true"
            />
        </div>
        <Paginator
            :page="page"
            :total="books.length"
            :per-page="10"
            @pageChange="onPageChange"
        />
    </div>
</template>
<script>
import Bookintro from "@/components/Bookintro";
import Paginator from "@/components/Paginator";
export default {
    name: "Author",
    components: { Bookintro, Paginator },
    props: {},
    computed: {
        books() {
            return this.$store.getters["getBooksByAuthor"](
                this.$route.params.name
            );
        },
    },
    data() {
        return {
            page: 1,
        };
    },
    mounted: function () {},
    methods: {
        onPageChange: function (page) {
            console.log(page);
        },
    },
};
</script>