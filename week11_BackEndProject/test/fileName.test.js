describe('fileName', () => {

    // before hook
    before(() => {
        console.log('before hook')
    })

    // beforeEach hook
    beforeEach(() => {
        console.log('beforeEach hook')
    })

    // after hook
    after(() => {
        console.log('after hook')
    })

    // afterEach hook
    afterEach(() => {
        console.log('afterEach hook')
    })

    describe('passing sumFunc()', () => {
        it('we expect a sum of 10 | expect style', () =>{
            expect(sumFunc([5,5])).to.equal(10)
            console.log('1st test')
        })
        it('we expect a sum of 10 | assert style', () =>{
            assert.equal(sumFunc([5,5]), 10, '5 + 5 = 10')
            console.log('2nd test')
        })
        it('we expect a sum of 10 | should style', () =>{
            result = sumFunc([5,5])
            result.should.equal(10)
            console.log('3rd test')
        })
    })

    describe('Test words variable', () => {
        it('I expect the variable words to hold the value "hello dear" | expect', () => {
            expect(words).to.equal('hello dear')
            console.log('4th test')
        })
        it('I expect the variable words to hold the value "hello dear" | assert', () => {
            assert.equal(words, 'hello dear', 'the variable words = hello dear')
            console.log('5th test')
        })
        it('I expect the variable words to hold the value "hello dear" | should', () => {
            words.should.equal('hello dear')
            console.log('6th test')
        })
    })

    describe('Check type', () => {
        it('we expect words to be a string | expect style', () => {
            expect(words).to.be.a('string')
            console.log('7th test')
        })
        it('we expect words to be a string | assert style', () => {
            assert.typeOf(words, 'string')
            console.log('8th test')
        })
        it('we expect words to be a string | should style', () => {
            result = typeof words 
            result.should.be.a('string')
            console.log('9th test')
        })
    })

    describe('failing sumFunc()', () =>{
        it('we expect failure', () =>{
            try{
                expect(sumFunc('five')).to.equal(5)
            }
            catch(error){
                console.log(error, 'you are in the catch')
            }
        })
    })
    // You can add .only or .skip after the describe or it blocks. This will either read only that set or skip it entirely.
})