<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <router-link class="navbar-brand" to="/">Dushu</router-link>
        <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
            @click="toggle"
        >
            <span class="navbar-toggler-icon"></span>
        </button>

        <div
            class="collapse navbar-collapse"
            id="navbarSupportedContent"
            :class="{ show: menuOpen }"
        >
            <ul class="navbar-nav mr-auto">
                <!-- <li class="nav-item">
                    <router-link class="nav-link" to="/">首页</router-link>
                    <span class="sr-only">(current)</span>
                </li> -->
                <li class="nav-item">
                    <router-link class="nav-link" to="/about/zhongguomingzhu">
                        中国名著
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/about/waiguomingzhu">
                        外国名著
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/about/wuxiaxiaoshuo">
                        武侠小说
                    </router-link>
                </li>
                <NarbarDD />
                <li class="nav-item">
                    <router-link class="nav-link" to="/about/wuxiaxiaoshuo">
                        拼音导航
                    </router-link>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input
                    class="form-control mr-sm-2 search"
                    type="search"
                    placeholder="请输入书名"
                    aria-label="Search"
                    v-model.trim="searchQuery"
                    @input="search"
                />
                <!-- <button
                    class="btn btn-outline-success my-2 my-sm-0"
                    type="submit"
                >
                    搜索
                </button> -->
                <div class="dropdown-list" v-if="matchedTitles.length">
                    <div class="nav nav-tabs" id="nav-tab" role="tablist">
                        <button
                            class="nav-link active"
                            id="nav-home-tab"
                            data-bs-toggle="tab"
                            data-bs-target="#nav-home"
                            type="button"
                            role="tab"
                            aria-controls="nav-home"
                            aria-selected="true"
                        >
                            Home
                        </button>
                        <button
                            class="nav-link"
                            id="nav-profile-tab"
                            data-bs-toggle="tab"
                            data-bs-target="#nav-profile"
                            type="button"
                            role="tab"
                            aria-controls="nav-profile"
                            aria-selected="false"
                        >
                            Profile
                        </button>
                        <button
                            class="nav-link"
                            id="nav-contact-tab"
                            data-bs-toggle="tab"
                            data-bs-target="#nav-contact"
                            type="button"
                            role="tab"
                            aria-controls="nav-contact"
                            aria-selected="false"
                        >
                            Contact
                        </button>
                    </div>
                </div>
            </form>
        </div>
    </nav>
</template>
<style lang="scss">
.navbar {
    a.navbar-brand,
    a.navbar-brand:hover,
    a.navbar-brand:active {
        color: #42b983;
    }
}
.navbar-light .navbar-nav .nav-link.router-link-active {
    color: rgba(0, 0, 0, 1);
    &:hover,
    &:focus {
        color: rgba(0, 0, 0, 1);
    }
}
form .search {
    transition: all 1s;
    width: 300px;
    &:focus {
        width: 300px;
        outline: none;
    }
}
@media (max-width: 991px) {
    // .navbar-toggler {
    // }
    form.form-inline {
        justify-content: space-between;
        input.form-control {
            flex: 1;
        }
    }
}
</style>
<script>
// @ is an alias to /src
import NarbarDD from "@/components/NarbarDD.vue";
import { mapGetters } from "vuex";
export default {
    name: "Narbar",
    components: { NarbarDD },
    computed: {
        ...mapGetters(["books"]),
    },
    data() {
        return {
            // submenus hide in mobile screen
            menuOpen: false,
            searchQuery: "",
            matchedTitles: [],
        };
    },
    mounted: function () {},
    methods: {
        toggle: function () {
            this.menuOpen = !this.menuOpen;
        },
        debounce: function (fn, time) {
            let timeId = null;
            return function (s) {
                if (timeId) clearTimeout(timeId);
                timeId = setTimeout(() => fn(s), time);
            };
        },
        search: function () {
            if (!this.searchQuery || !this.books) return;
            const regex = new RegExp(this.searchQuery, "gi");
            this.matchedTitles = this.books.filter((book) =>
                regex.test(book.title)
            );
            console.log(this.matchedTitles);
        },
    },
};
</script>