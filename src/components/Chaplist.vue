<template>
    <nav aria-label="Page navigation bg-dark">
        <ul class="pagination pagination-sm">
            <li
                class="page-item"
                v-for="(v, i) in letters"
                :key="i"
                :class="{ active: v === page }"
            >
                <router-link class="page-link" :to="'/pinyin/' + v">
                    {{ v }}
                </router-link>
            </li>
        </ul>
    </nav>
</template>
<style lang="scss" scoped>
.pagination {
    justify-content: space-between;
    overflow-y: hidden;
}
.page-link {
    background: none;
    color: var(--gray-dark);
    border: 1px solid #aaa;
}
</style>
<script>
export default {
    name: "PaginatorAZ",
    props: {
        page: {
            type: String,
            default: "A",
        },
    },
    computed: {
        letters() {
            return Array.from({ length: 26 }).map((_, i) =>
                String.fromCharCode(i + 65)
            );
        },
    },
};
</script>