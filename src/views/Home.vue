<template>
    <h2>下载排行榜</h2>
    <div class="books">
        <Bookintro
            v-for="book in mostDownloadedBooks"
            :key="book.id"
            :book="book"
            :cat-show="true"
        />
    </div>
</template>
<script>
import { mapGetters } from "vuex";
import Bookintro from "@/components/Bookintro";
export default {
    name: "Home",
    components: {
        Bookintro,
    },
    props: {},
    computed: {
        ...mapGetters(["mostDownloadedBooks"]),
    },
    methods: {},
};
</script>
