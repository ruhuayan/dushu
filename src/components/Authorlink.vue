<template>
    <div class="author_category">
        <div class="author">
            <span>作者：</span>
            <router-link :to="'/author/' + author" v-if="author">
                {{ author }}
            </router-link>
            <span v-else>无名</span>
        </div>
        <div class="category">
            <span>种类：</span>
            <router-link :to="`/about/${category}`">
                {{ categoryCn }}
            </router-link>
        </div>
    </div>
</template>
<script>
export default {
    name: "Authorlink",
    props: {
        author: {
            type: String,
        },
        category: {
            type: String,
        },
        categoryCn: {
            type: String,
        },
    },
};
</script>