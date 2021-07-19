import { mutations, actions, getters } from '@/store'

describe('mutations', () => {
	it('SET_LOADING', () => {
		// mock state
		const state = { loading: false }
		// apply mutation
		mutations.SET_LOADING(state, true)
		// assert result
		expect(state).toEqual({ loading: true });
	})

	it('SAVE_BOOKS', async () => {
		const state = { books: [] }
		const mockBooks = {
			books: [{
				id: 123,
			}, {
				id: 124
			}]
		};
		await mutations.SAVE_BOOKS(state, mockBooks);
		expect(state.books).toBe(mockBooks.books)
	})
});

describe('getters', () => {
	it('books', () => {
		// mock state
		const state = {
			books: [{ id: 123, }, { id: 124 }],
			loading: false
		}

		const result = getters.books(state)

		expect(result).toEqual([{ id: 123, }, { id: 124 }])
	})
});

describe('actions', () => {
	it('tests with a mock commit', async () => {
		const state = {
			books: [],
			loading: true,
		}
		let mockCommit = (_, payload) => {
			console.log(payload)
			state.books = payload
			state.loading = false
		}
		actions.loadBooks({ state, commit: mockCommit }, 'mock').then(() => {
			expect(state.loading).toBe(true)
			expect(state.books).toEqual([{ id: 123, }, { id: 124 }])
		}).catch(err => console.log(err));
	})
})