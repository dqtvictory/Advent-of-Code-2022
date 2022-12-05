# from collections.abc import Iterable
# from typing import TypeVar
from copy import copy
from functools import reduce


# TGeneric = TypeVar("TGeneric")
# TContainer = TypeVar("TContainer")


class Chainable:
	def __init__(self, iterable):
		self.__iterable = iterable

	def __iter__(self):
		return self.__iterable
	
	def collect(self, container_t=list):
		""" Return a shallow copy of the inner iterable. If `container_t` is specified
		then the iterable is collected as the desired type, otherwise default to a list """
		it = copy(self.__iterable)
		return container_t(it)

	def map(self, map_func):
		return Chainable(
			map(map_func, self.__iterable)
		)

	def flat_map(self, map_func):
		it = []
		for elem in map(map_func, self.__iterable):
			it += list(elem)
		return Chainable(it)

	def reduce(self, red_func, init=False, initial=None):
		if init:
			return reduce(red_func, self.__iterable, initial)
		return reduce(red_func, self.__iterable)

	def filter(self, fil_func):
		return Chainable(
			filter(fil_func, self.__iterable)
		)

	def sort(self, key=None, desc=False):
		return Chainable(
			sorted(self.__iterable, key=key, reverse=desc)
		)

	def zip(self, other):
		if isinstance(other, Chainable):
			return Chainable(
				zip(self.__iterable, other.__iterable)
			)
		return Chainable(
			zip(self.__iterable, other)
		)

	def enumerate(self, start=0):
		return Chainable(
			enumerate(self.__iterable, start)
		)
