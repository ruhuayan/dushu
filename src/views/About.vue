<template>
    <div class="about">
        <h1>{{ categoryCn }}</h1>
        <div class="books">
            <div class="book" v-for="book in books" :key="book.id">
                <div class="bookTitle">
                    <router-link :to="'/book/' + book.id">{{
                        book.title
                    }}</router-link>
                </div>
                <div class="bookDesc">{{ book.description }}</div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "About",
    components: {},
    props: {},
    computed: {
        books() {
            return this.$store.getters["getBookByCategory"](
                this.$route.params.category
            );
        },
        categoryCn() {
            const categories = {
                zhongguomingzhu: "中国名著",
                waiguomingzhu: "外国名著",
                wuxiaxiaoshuo: "武侠小说",
                gudianmingzhu: "古典名著",
                mingrenzhuanji: "名人传记",
                tonghua: "儿童文学",
                gushi: "经典故事",
                jiaoyu: "教育励志",
                shici: "诗词散文",
                qtyd: "其它阅读",
            };
            return categories[this.$route.params.category];
        },
    },
    data() {
        return {};
    },
    mounted: function () {},
    methods: {},
};
</script>