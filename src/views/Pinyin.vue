<template>
    <div class="booklist">
        <PaginatorAZ :page="letter" />
        <h2>
            {{ letter }} 字头小说
            <span>(共{{ books.length }}部)</span>
        </h2>
        <div class="books mb-5" v-if="books.length">
            <Bookintro v-for="book in books" :key="book.id" :book="book" />
        </div>
        <div class="books mb-5" v-else>没有书</div>
    </div>
</template>
<script>
import Bookintro from "@/components/Bookintro";
import PaginatorAZ from "@/components/PaginatorAZ";
export default {
    name: "About",
    components: { Bookintro, PaginatorAZ },
    title() {
        return `拼音导航 - ${this.letter}`;
    },
    computed: {
        letter() {
            return this.$route.params.letter
                ? this.$route.params.letter.toUpperCase()
                : "A";
        },
        books() {
            return this.$store.getters["getBooksByLetter"](this.letter);
        },
    },
};
</script>