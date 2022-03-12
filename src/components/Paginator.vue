<template>
    <nav aria-label="Page navigation" v-if="max > 1">
        <ul class="pagination justify-content-center">
            <li class="page-item" :class="{ disabled: currentPage === 1 }">
                <a
                    class="page-link"
                    href="javascript:;"
                    tabindex="-1"
                    @click="onPageChange('prev')"
                    >{{ prev }}</a
                >
            </li>
            <li
                class="page-item"
                v-for="(v, i) in pages"
                :key="i"
                :class="{ active: v === currentPage }"
            >
                <a
                    class="page-link"
                    @click="onPageChange(v, i)"
                    href="javascript:;"
                    >{{ v }}</a
                >
            </li>
            <li class="page-item" :class="{ disabled: currentPage === max }">
                <a
                    class="page-link"
                    href="javascript:;"
                    @click="onPageChange('next')"
                    >{{ next }}</a
                >
            </li>
        </ul>
    </nav>
</template>
<script>
export default {
    name: "Paginator",
    props: {
        page: {
            type: Number,
            default: 1,
        },
        total: {
            type: Number,
            required: true,
        },
        perPage: {
            type: Number,
            default: 10,
        },
        prev: {
            type: String,
            default: "Prev",
        },
        next: {
            type: String,
            default: "Next",
        },
    },
    computed: {
        max() {
            return Math.ceil(this.total / this.perPage);
        },
    },
    data() {
        return {
            currentPage: this.page,
            pages: [],
        };
    },
    methods: {
        onPageChange: function (v, i = null) {
            if (v === "prev") this.currentPage -= 1;
            else if (v === "next") this.currentPage += 1;
            else if (v === "...") {
                // jump 2 pages from prev page
                this.currentPage = this.pages[i - 1] + 1;
            } else if (v >= 1) {
                this.currentPage = v;
            }
            if (this.max >= 10) {
                this.pages = this.formatPages(this.currentPage);
            }
            this.$emit("pageChange", this.currentPage);
        },
        formatPages: function (v) {
            if (this.max < 10)
                return Array.from({ length: this.max }).map((_, i) => i + 1);

            if (v <= 3) {
                return [1, 2, 3, 4, "...", this.max];
            } else if (v >= this.max - 1) {
                return [1, 2, "...", this.max - 2, this.max - 1, this.max];
            } else {
                return [1, "...", v - 1, v, v + 1, "...", this.max];
            }
        },
    },
    watch: {
        page: function (val) {
            this.currentPage = val;
        },
        max: function () {
            this.pages = this.formatPages(this.currentPage);
        },
    },
    mounted: function () {
        this.pages = this.formatPages(this.currentPage);
    },
};
</script>