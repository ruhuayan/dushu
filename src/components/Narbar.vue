<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <router-link class="navbar-brand" to="/">
            <img
                class="dushuIcon"
                src="img/dushu296x240.png"
                alt="Dushu icon"
            />
        </router-link>
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
                <NarbarDD :dd-show="ddShow" ref="dropdown" />
                <li class="nav-item">
                    <router-link class="nav-link" to="/pinyin/A">
                        拼音导航
                    </router-link>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0" ref="searchForm">
                <div class="input-group">
                    <input
                        class="form-control sm-2 search"
                        type="search"
                        placeholder="请输入书名"
                        aria-label="Search"
                        v-model.trim="searchQuery"
                        @input="onInputChange"
                    />
                    <div class="input-group-append">
                        <button
                            class="btn btn-search"
                            type="button"
                            @click="search"
                        >
                            <img
                                src="data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHZpZXdCb3g9IjAgMCAxNzIgMTcyIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9Im5vbnplcm8iIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtbGluZWNhcD0iYnV0dCIgc3Ryb2tlLWxpbmVqb2luPSJtaXRlciIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBzdHJva2UtZGFzaGFycmF5PSIiIHN0cm9rZS1kYXNob2Zmc2V0PSIwIiBmb250LWZhbWlseT0ibm9uZSIgZm9udC13ZWlnaHQ9Im5vbmUiIGZvbnQtc2l6ZT0ibm9uZSIgdGV4dC1hbmNob3I9Im5vbmUiIHN0eWxlPSJtaXgtYmxlbmQtbW9kZTogbm9ybWFsIj48cGF0aCBkPSJNMCwxNzJ2LTE3MmgxNzJ2MTcyeiIgZmlsbD0ibm9uZSI+PC9wYXRoPjxnIGZpbGw9IiMzMzMzMzMiPjxwYXRoIGQ9Ik02NC41LDE0LjMzMzMzYy0yNy42MjE0LDAgLTUwLjE2NjY3LDIyLjU0NTI3IC01MC4xNjY2Nyw1MC4xNjY2N2MwLDI3LjYyMTQgMjIuNTQ1MjcsNTAuMTY2NjcgNTAuMTY2NjcsNTAuMTY2NjdjMTIuNTI3MzIsMCAyMy45NzI1NiwtNC42NzI0OSAzMi43ODE5LC0xMi4zMTc3MWwzLjA1MTQzLDMuMDUxNDN2OS4yNjYyOGw0Myw0M2wxNC4zMzMzMywtMTQuMzMzMzNsLTQzLC00M2gtOS4yNjYyOGwtMy4wNTE0MywtMy4wNTE0M2M3LjY0NTIxLC04LjgwOTM0IDEyLjMxNzcxLC0yMC4yNTQ1OCAxMi4zMTc3MSwtMzIuNzgxOWMwLC0yNy42MjE0IC0yMi41NDUyNywtNTAuMTY2NjcgLTUwLjE2NjY3LC01MC4xNjY2N3pNNjQuNSwyOC42NjY2N2MxOS44NzUwOSwwIDM1LjgzMzMzLDE1Ljk1ODI0IDM1LjgzMzMzLDM1LjgzMzMzYzAsMTkuODc1MDkgLTE1Ljk1ODI1LDM1LjgzMzMzIC0zNS44MzMzMywzNS44MzMzM2MtMTkuODc1MDksMCAtMzUuODMzMzMsLTE1Ljk1ODI1IC0zNS44MzMzMywtMzUuODMzMzNjMCwtMTkuODc1MDkgMTUuOTU4MjQsLTM1LjgzMzMzIDM1LjgzMzMzLC0zNS44MzMzM3oiPjwvcGF0aD48L2c+PC9nPjwvc3ZnPg=="
                                alt="icon"
                                width="24"
                                height="24"
                            />
                        </button>
                    </div>
                </div>
                <div
                    class="dropdown-list"
                    v-if="
                        (searchResult.title.length ||
                            searchResult.author.length) &&
                        !closeSearch
                    "
                >
                    <ul class="nav nav-tabs" id="myTab" role="tablist">
                        <li class="nav-item">
                            <a
                                class="nav-link"
                                :class="{ active: searchType === 'title' }"
                                id="home-tab"
                                data-toggle="tab"
                                href="javascript:;"
                                role="tab"
                                aria-controls="home"
                                :aria-selected="searchType === 'title'"
                                @click="setSearchType('title')"
                                >书名
                            </a>
                        </li>
                        <li class="nav-item">
                            <a
                                class="nav-link"
                                :class="{ active: searchType === 'author' }"
                                id="profile-tab"
                                data-toggle="tab"
                                href="javascript:;"
                                role="tab"
                                aria-controls="profile"
                                :aria-selected="searchType === 'author'"
                                @click="setSearchType('author')"
                                >作者
                            </a>
                        </li>
                    </ul>
                    <div class="bookList">
                        <template v-if="matchedBooks.length">
                            <div
                                class="book"
                                v-for="book in matchedBooks"
                                :key="book.id"
                            >
                                <router-link :to="`/book/${book.id}`">
                                    {{ book.title }}
                                </router-link>
                                <span class="book-author">
                                    (作者：
                                    <router-link :to="'/author/' + book.author">
                                        {{ book.author }}
                                    </router-link>
                                    )
                                </span>
                            </div>
                        </template>
                        <div class="book" v-else>
                            没有找到
                            {{
                                searchType === "author"
                                    ? "该作者的书"
                                    : "相关书"
                            }}
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </nav>
</template>
<style lang="scss" scoped>
.navbar {
    a.navbar-brand,
    a.navbar-brand:hover,
    a.navbar-brand:active {
        color: #42b983;
    }
}
.nav-link.router-link-active {
    cursor: default;
}
.navbar-dark .navbar-nav .nav-link.router-link-active {
    color: rgba(255, 255, 255, 0.9);
}
.navbar-light .navbar-nav .nav-link.router-link-active {
    color: rgba(0, 0, 0, 1);
    &:hover,
    &:focus {
        color: rgba(0, 0, 0, 1);
    }
}
img.dushuIcon {
    width: 36px;
    height: auto;
}
form .search {
    transition: all 1s;
    width: 300px;
    box-shadow: none;
    &:focus {
        width: 300px;
        outline: none;
    }
}
.btn-search {
    padding: 0 0.5em;
    background: #eee;
}

.dropdown-list {
    position: absolute;
    top: 50px;
    background: #fff;
    width: 300px;
    border-radius: 0.3rem;
    .bookList {
        height: 340px;
        overflow-y: auto;
        &::-webkit-scrollbar {
            width: 8px;
        }
    }
    .book {
        padding: 0.2rem 0.5rem;
        margin: 0;
        &:first-child {
            margin-top: 0.5rem;
        }
        .book-author {
            font-size: 12px;
            color: #999;
            margin-left: 0.5rem;
        }
    }
}
@media (max-width: 991px) {
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
import { debounced } from "../models/debounced";
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
            ddShow: false,
            searchQuery: "",
            matchedBooks: [],
            searchType: "title",
            searchResult: {
                title: [],
                author: [],
            },
            closeSearch: false,
        };
    },
    mounted: function () {
        document.addEventListener("click", this.onClose);
        this.debouncedListener = debounced(this.searchFunc, 1000).bind(this);
    },
    unmounted: function () {
        document.removeEventListener("click", this.onClose);
    },
    methods: {
        toggle: function () {
            this.menuOpen = !this.menuOpen;
        },
        search: function () {
            if (!this.searchQuery) return;

            this.$router.push({
                path: "/search",
                query: { book: this.searchQuery, qtype: this.searchType },
            });
            setTimeout(() => (this.closeSearch = true), 500);
        },
        onInputChange: function () {
            // debounced - 1s
            this.debouncedListener();
        },
        searchFunc: function () {
            if (!this.searchQuery || !this.books) {
                this.resetSearch();
                return;
            }
            const regex = new RegExp(this.searchQuery, "gi");

            const booksByTitle = this.books
                .filter((book) => regex.test(book.title))
                .sort(
                    (a, b) => b.download_ebook_count - a.download_ebook_count
                );
            const booksByAuthor = this.books
                .filter((book) => regex.test(book.author))
                .sort(
                    (a, b) => b.download_ebook_count - a.download_ebook_count
                );
            this.searchResult = {
                title: booksByTitle,
                author: booksByAuthor,
            };

            this.matchedBooks = this.searchResult[this.searchType];
            this.$store.dispatch("searchBook", this.searchQuery);
        },
        setSearchType: function (type) {
            this.searchType = type;
            this.matchedBooks = this.searchResult[type];
        },
        resetSearch: function () {
            this.matchedBooks = [];
            this.searchResult = {
                title: [],
                author: [],
            };
        },
        onClose: function (event) {
            // clicks on search form
            if (this.$refs.searchForm.contains(event.target)) {
                this.closeSearch = false;
            } else {
                this.closeSearch = true;
            }
            // clicks on dropdown
            if (this.$refs.dropdown.$el.contains(event.target)) {
                this.ddShow = !this.ddShow;
            } else {
                this.ddShow = false;
            }
        },
    },
};
</script>