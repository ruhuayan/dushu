<template>
    <div class="book">
        <div class="bookTitle">
            <router-link :to="`/book/${book.id}`">{{ book.title }}</router-link>
        </div>
        <authorlink
            :author="book.author"
            :category="book.category"
            :category-cn="Categories[book.category]"
        />

        <div class="bookDesc">{{ book.description }}</div>
        <Downloadlink :book="book" />
    </div>
</template>
<script>
import Authorlink from "@/components/Authorlink";
import Downloadlink from "@/components/Downloadlink";
import { Categories } from "../models/categories";

export default {
    name: "Bookintro",
    components: { Authorlink, Downloadlink },
    props: {
        book: {
            type: Object,
            required: true,
        },
    },
    computed: {
        Categories() {
            return Categories;
        }
    },
};
</script>