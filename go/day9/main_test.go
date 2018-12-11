package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func Test_parse(t *testing.T) {
	p, m := parse("13 players; last marble is worth 55 points", 1)

	assert.EqualValues(t, 13, p)
	assert.EqualValues(t, 55, m)
}

func Test_parse_factor(t *testing.T) {
	p, m := parse("13 players; last marble is worth 55 points", 10)

	assert.EqualValues(t, 13, p)
	assert.EqualValues(t, 550, m)
}

func Test_run(t *testing.T) {
	assert.Equal(t, 32, run(9, 25))
	assert.Equal(t, 8317, run(10, 1618))
	assert.Equal(t, 146373, run(13, 7999))
	assert.Equal(t, 2764, run(17, 1104))
	assert.Equal(t, 54718, run(21, 6111))
	assert.Equal(t, 37305, run(30, 5807))
}
