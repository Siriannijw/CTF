	.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #16				// SP = -64
	str	w0, [sp, 12]			// SP+12 = w0 -> 182,476,535
	str	w1, [sp, 8]				// SP+8 = w1 -> 3,742,084,308
	ldr	w1, [sp, 12]			// w1 = SP+12 -> 182,476,535
	ldr	w0, [sp, 8]				// w0 = SP+8 -> 3,742,084,308
	cmp	w1, w0					// cmp 182,476,535 3,742,084,308
	bls	.L2						// Branch lower or same .L2
	ldr	w0, [sp, 12]			// w0 = sp+12 -> 182,476,535
	b	.L3l					// Branch .L3
.L2:
	ldr	w0, [sp, 8]				// w0 -> 3,742,084,308
.L3:
	add	sp, sp, 16				// SP = -48
	ret							// Returns 3,742,084,308
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!	// stack pointer (SP) = -48
								// SP = x29 : frame pointer (FP)
								// SP+8 = x30 : link register (LR)
	add	x29, sp, 0				// FP = SP
	str	x19, [sp, 16]			// SP+16 = x19
	str	w0, [x29, 44]			// SP+44 = w0 -> "182,476,535"
	str	x1, [x29, 32]			// SP+32 = x1 -> "3,742,084,308"
	ldr	x0, [x29, 32]			// x0 = SP+32
	add	x0, x0, 8				// x0 = SP+40
	ldr	x0, [x0]				// x0 = *SP+40
	bl	atoi					// atoi "182,476,535"
	mov	w19, w0					// x19 = w0 -> 182,476,535
	ldr	x0, [x29, 32]			// x0 = SP+32
	add	x0, x0, 16				// x0 = SP+48
	ldr	x0, [x0]				// x0 = *SP+48
	bl	atoi					// atoi "3,742,084,308"
	mov	w1, w0					// w1 = w0 -> 3,742,084,308
	mov	w0, w19					// w0 = w19 -> 182,476,535
	bl	func1					// Call func1
	mov	w1, w0					// w1 = w0
	adrp	x0, .LC0			// Page Address of .LC0
	add	x0, x0, :lo12:.LC0		// Load .LC0 into x0
	bl	printf					// printf "Result: %ld\n" 3742084308
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
