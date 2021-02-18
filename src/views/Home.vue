<template>
    <div class="contontTitle">下载排行榜</div>
    <div class="books">
        <div class="book" v-for="book in mostDownloadedBooks" :key="book.id">
            <div class="bookTitle">
                <router-link :to="'/book/' + book.id">{{
                    book.title
                }}</router-link>
            </div>
            <div class="bookDesc">{{ book.description }}</div>
        </div>
    </div>
</template>
<style lang="scss">
.contontTitle {
    font-size: 24px;
    font-weight: bold;
}
.book {
    margin-top: 1rem;
}
.bookTitle {
    font-weight: bold;
}
.bookDesc {
    font-size: 0.9rem;
}
</style>
<script>
import { mapGetters } from "vuex";
export default {
    name: "Home",
    components: {},
    props: {},
    computed: {
        ...mapGetters(["mostDownloadedBooks"]),
    },
    methods: {},
};
</script>
