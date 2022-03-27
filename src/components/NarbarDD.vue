<template>
    <li class="nav-item dropdown">
        <a
            class="nav-link dropdown-toggle"
            href="javascript:;"
            id="navbarDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
        >
            {{ categoryCn }}
        </a>
        <div
            class="dropdown-menu"
            :class="{ show: show }"
            aria-labelledby="navbarDropdown"
        >
            <!-- <div class="dropdown-divider"></div> -->
            <router-link
                v-for="(value, name) in categories"
                :key="name"
                class="dropdown-item"
                :to="'/about/' + name"
                :class="{ active: categoryCn === value }"
            >
                {{ value }}
            </router-link>
        </div>
    </li>
</template>
<script>
export default {
    name: "NarbarDD",
    props: {
        ddShow: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            show: false,
            categoryCn: "",
        };
    },
    computed: {
        categories() {
            return {
                gudianmingzhu: "古典名著",
                mingrenzhuanji: "名人传记",
                tonghua: "儿童文学",
                gushi: "经典故事",
                jiaoyu: "教育励志",
                shici: "诗词散文",
                qtyd: "其它阅读",
            };
        },
    },
    watch: {
        $route(route) {
            this.categoryCn = this.categories[route.params.category] || "其它";
        },
        ddShow(val) {
            this.show = val;
        },
    },
};
</script>