<template>
    <footer class="text-center text-lg-start bg-dark text-light">
        <div class="container p-4">
            <!--Grid row-->
            <div class="row">
                <!--Grid column-->
                <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
                    <h5 class="text-uppercase">推荐书籍</h5>

                    <p class="booklist">
                        <span v-for="book of books.selected" :key="book.id">
                            <router-link :to="`/book/${book.id}`">
                                {{ book.title }}
                            </router-link>
                        </span>
                    </p>
                </div>
                <!--Grid column-->

                <!--Grid column-->
                <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
                    <h5 class="text-uppercase">{{ categoryCn }}</h5>

                    <p class="booklist">
                        <span
                            v-for="book of categoryBooks.selected"
                            :key="book.id"
                        >
                            <router-link :to="`/book/${book.id}`">
                                {{ book.title }}
                            </router-link>
                        </span>
                    </p>
                </div>
                <!--Grid column-->
            </div>
            <!--Grid row-->
        </div>

        <div class="text-center p-3 copyright bg-dark">
            © 2020 - 2021 Dushu
            <br />
            Powered by <a href="https://richyan.com/">richyan.com</a>
        </div>
    </footer>
</template>
<script>
import { Categories } from "../models/categories";
export default {
    name: "Footer",
    computed: {
        books() {
            return this.$store.getters["mostDownloadedBooks"](1, 20);
        },
        category() {
            const categories = Object.keys(Categories);
            const rand = Math.floor(Math.random() * categories.length);
            return categories[rand];
        },
        categoryCn() {
            return Categories[this.category];
        },
        categoryBooks() {
            return this.$store.getters["getBooksByCategory"](
                this.category,
                1,
                20
            );
        },
    },
};
</script>
<style scoped lang="scss">
p.booklist span a {
    color: #fff;
    margin: 0 8px;
    font-size: 14px;
    display: inline-block;
}
.copyright {
    font-size: 12px;
}
</style>
